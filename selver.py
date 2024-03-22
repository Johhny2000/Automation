import requests
from bs4 import BeautifulSoup


def search_selver(product_name):
    base_url = "https://www.selver.ee/"
    search_url = f"{base_url}search?"
    params = {"q": product_name}

    # Make a request to the search page
    response = requests.get(search_url, params=params)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract product information
        product_list = []
        for product_div in soup.find_all('div', class_='product'):
            name = product_div.find('div', class_='product__name').text.strip()
            price_str = product_div.find('div', class_='product__price').text.strip()
            price = float(''.join(filter(str.isdigit, price_str))) / 100  # Convert price to float

            product_list.append({"name": name, "price": price})

        # Sort products by price in ascending order
        sorted_products = sorted(product_list, key=lambda x: x["price"])

        # Return the top 5 cheapest products
        return sorted_products[:5]
    else:
        print(f"Error {response.status_code}: Unable to fetch data from Selver.ee")
        return None


if __name__ == "__main__":
    product_name = input("Enter the product name: ")
    search_results = search_selver(product_name)

    if search_results:
        print("\nTop 5 Cheapest Matches:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result['name']} - €{result['price']:.2f}")
