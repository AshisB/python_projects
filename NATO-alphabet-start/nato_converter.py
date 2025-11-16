nato = {
    'A':'Alpha','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo','F':'Foxtrot',
    'G':'Golf','H':'Hotel','I':'India','J':'Juliet','K':'Kilo','L':'Lima','M':'Mike',
    'N':'November','O':'Oscar','P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra',
    'T':'Tango','U':'Uniform','V':'Victor','W':'Whiskey','X':'X-ray','Y':'Yankee','Z':'Zulu',
    '0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine',
    '&':'Ampersand','*':'Asterisk','@':'At','#':'Hash',' ':'Space',
    '.':'Dot', ',':'Comma', '-':'Dash', '_':'Underscore', '+':'Plus', '=':'Equals',
    '/':'Slash', '\\':'Backslash', ':':'Colon', ';':'Semicolon', '!':'Exclamation',
    '?':'Question', '"':'Double Quote', "'":'Single Quote', '(':'Left Parenthesis', 
    ')':'Right Parenthesis', '[':'Left Bracket', ']':'Right Bracket', '{':'Left Brace', 
    '}':'Right Brace', '<':'Less Than', '>':'Greater Than', '|':'Vertical Bar',
    '~':'Tilde', '`':'Backtick', '$':'Dollar', '%':'Percent', '^':'Caret'
}

print("=== NATO CONVERTER ===")
while True:
    text = input("Enter text: ").strip().upper()
    if text == 'QUIT': break
    for char in text:
        if char in nato:
            print(f"  {char} => {nato[char]}")
        else:
            print(f"  {char} ")
    print()