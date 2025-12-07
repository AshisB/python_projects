import base64
import json
from collections import Counter

# Your encrypted data
encrypted_b64 = "FlsRQ0lTDBITFyhYQR0AGBgAARkWXjIXIV9bXgwbEQ8YXRRfH0Z6ERAaXE8XLhk/T2I4BRp/AxhbWw1NU1EVEkhEOxNBVwwKFENJU1UJRQtrQV9QFSFFUyBVPHk4UDgTTx9NWxQSFVFNEAlGM1VUEVdZUlY/UEYCEBIve1VHXDAEQEIYVU0P"

# Decode from base64
encrypted_bytes = base64.b64decode(encrypted_b64)
print(f"Data length: {len(encrypted_bytes)} bytes")


# Analyze for XOR key length using index of coincidence
def find_key_length(ciphertext, max_len=20):
    """Find likely XOR key length"""
    results = []
    for key_len in range(1, min(max_len, len(ciphertext))):
        # Take every key_len-th byte
        sequences = []
        for i in range(key_len):
            seq = ciphertext[i::key_len]
            sequences.append(seq)

        # Calculate average frequency
        avg_freq = 0
        for seq in sequences:
            freq = Counter(seq)
            # English text has certain byte frequencies
            # Common bytes in JSON: 34=", 58=:, 44=,, 123={, 125=}, 91=[, 93=]
            common_bytes = [34, 58, 44, 123, 125, 91, 93, 32]
            score = sum(freq.get(b, 0) for b in common_bytes)
            avg_freq += score / len(seq)

        avg_freq /= key_len
        results.append((key_len, avg_freq))

    # Sort by best score (higher = more like English/JSON)
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:5]


print("\n🔍 Analyzing for key length...")
possible_lengths = find_key_length(encrypted_bytes)
for length, score in possible_lengths:
    print(f"  Key length {length}: score {score:.3f}")

# Try the most likely key lengths
print("\n🔓 Trying to decrypt with likely key lengths...")

# Common patterns in password manager JSON
common_phrases = [
    b'"website"', b'"email"', b'"password"',
    b'gmail.com', b'yahoo.com', b'hotmail.com',
    b'facebook', b'google', b'amazon',
    b'user', b'username', b'login'
]

for key_len, _ in possible_lengths[:3]:
    print(f"\nTrying key length {key_len}:")

    # Break into key_len columns
    columns = []
    for i in range(key_len):
        columns.append(encrypted_bytes[i::key_len])

    # Try to guess each byte of the key
    possible_key = bytearray(key_len)

    for i in range(key_len):
        col = columns[i]
        best_byte = 0
        best_score = 0

        # Try every possible byte (0-255)
        for byte in range(256):
            # Decrypt this column with this byte
            decrypted_col = bytes([c ^ byte for c in col])

            # Score based on printable ASCII and common phrases
            score = 0
            for b in decrypted_col:
                if 32 <= b <= 126:  # Printable ASCII
                    score += 1
                if b == 34 or b == 58 or b == 44:  # " : , common in JSON
                    score += 2

            # Check for common phrases
            text = decrypted_col.decode('ascii', errors='ignore').lower()
            for phrase in common_phrases:
                if phrase.decode().lower() in text:
                    score += 10

            if score > best_score:
                best_score = score
                best_byte = byte

        possible_key[i] = best_byte

    key = bytes(possible_key)
    print(f"  Possible key: {key} (as text: {key.decode('ascii', errors='ignore')})")

    # Try to decrypt with this key
    decrypted = bytearray()
    for i, byte in enumerate(encrypted_bytes):
        decrypted.append(byte ^ key[i % key_len])

    try:
        text = decrypted.decode('utf-8')
        # Check if it looks like JSON
        if text.startswith('{') and text.endswith('}'):
            print(f"  ✅ Looks like JSON!")
            print(f"  Preview: {text[:100]}...")

            # Try to parse
            try:
                data = json.loads(text)
                print(f"  ✅ Valid JSON! Contains {len(data)} entries")
                for website in list(data.keys())[:3]:
                    print(f"    - {website}: {data[website].get('email', 'No email')}")
            except:
                print(f"  ❌ Not valid JSON")
    except:
        continue

# Brute force with common password keys
print("\n🎯 Brute forcing with common password patterns...")
common_passwords = [
    # Short passwords
    b'pass', b'word', b'1234', b'admin', b'root', b'guest',
    b'test', b'temp', b'demo', b'user', b'login',

    # Your possible passwords
    b'master', b'password', b'secret', b'private',
    b'key', b'lock', b'safe', b'vault',

    # Longer possibilities
    b'masterpass', b'mypassword', b'mysecret',
    b'password123', b'admin123', b'root123',
]

for pwd in common_passwords:
    # Try different key lengths based on password
    for key_len in [len(pwd), 8, 12, 16]:
        if key_len > len(encrypted_bytes):
            continue

        # Create repeating key
        key = (pwd * (key_len // len(pwd) + 1))[:key_len]

        decrypted = bytearray()
        for i, byte in enumerate(encrypted_bytes):
            decrypted.append(byte ^ key[i % key_len])

        try:
            text = decrypted.decode('utf-8')
            if '"website"' in text or '"email"' in text or '"password"' in text:
                print(f"\n🔓 FOUND! Key: {pwd.decode()} (length: {key_len})")
                print(f"Decrypted preview: {text[:150]}...")

                # Show structure
                lines = text.split(',')
                for line in lines[:5]:
                    if 'website' in line or 'email' in line or 'password' in line:
                        print(f"  {line.strip()}")
                break
        except:
            continue