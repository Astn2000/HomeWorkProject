from src.masks import mask_account_card
from src.masks import get_date


if __name__ == "__main__":
    print(mask_account_card("Visa Gold", "5999414228426353"))
    print(mask_account_card("Счет", "64686473678894779589"))
    print(get_date("2024-03-11T02:26:18.671407"))
