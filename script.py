


if __name__ == '__main__':
    url = "https://dummyjson.com/products"
    response = http_get(url)
    print(response)

    # res = read_params()
    # print(res)

    # python3 main.py --protocol http --hostname google.com --uri /fr --threshold 1
    res = format_url("https", "google.com", "/fr")
    print(res)
