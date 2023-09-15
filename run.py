from whatsapp_api_client_python import API

greenAPI = API.GreenApi(
    "7103857810", "dd5c9e0570bb4f62af571de2fae1eb1cb3c415ed4051410e99"
)


def main():
    response = greenAPI.sending.sendMessage("+77072777069@c.us", "asdasdas")

    print(response.data)


if __name__ == '__main__':
    main()