THRESHOLD=50


from fuzzywuzzy import  fuzz

class Scraping:
    def __init__(self,soup):
        self.soup=soup
        self.address=[]
        self.price=[]
        self.link=[]
        self.start_scraping_with_bs4()



    def start_scraping_with_bs4(self):
        print('Scraping initiated...')

        # Scraping price
        price_list=self.soup.select('[data-test="property-card-price"]')
        self.price=[price.string.split("+")[0].split("/")[0] for price in price_list]
        print(self.price)

        # Scraping  link
        link_list=self.soup.select('.StyledPropertyCardDataArea-anchor')
        self.link=[link.get('href') for link in link_list if link.get('href')]
        print(self.link)

        #Scraping address
        address_list=self.soup.select('[data-test="property-card-addr"]')
        filtered_address=[address.string.replace("\n","").replace("  ","").replace("|",",").strip() for address in address_list]
        print(self.address)
        for address in filtered_address:
            parts = address.split(",")
            if len(parts)>=2:
                first=parts[0].strip()
                second=parts[1].strip()
                if fuzz.ratio(first,second)>=THRESHOLD:#fuzzy logic imported to check similarities
                    final_address = ",".join(parts[1:]).strip()
                else:
                    final_address=address
            else:
                final_address = address

            self.address.append(final_address)

        print(self.address)