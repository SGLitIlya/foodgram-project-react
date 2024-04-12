EMAIL_MAX_LEN: int = 254
PASSWORD_MAX_LEN: int = 150
USERNAME_MAX_LEN: int = 150
FIRST_NAME_MAX_LEN: int = 150
LAST_NAME_MAX_LEN: int = 150

RECIPE_NAME_MAX_LEN: int = 200
TAG_NAME_MAX_LEN: int = 200
TAG_SLUG_MAX_LEN: int = 200
ING_NAME_MAX_LEN: int = 200
ING_MES_MAX_LEN: int = 200
TAG_COLOR_MAX_LEN: int = 7
RECIPE_CKN_TIME_MIN: int = 1
ING_AMOUNT_MIN: int = 1
RECIPE_CKN_TIME_MAX: int = 32
ING_AMOUNT_MAX: int = 32

RECIPE_CKN_TIME_MIN_ERR_MSG: str = (
    f'Время приготовления рецепта не может быть < {RECIPE_CKN_TIME_MIN}.'
)
RECIPE_CKN_TIME_MAX_ERR_MSG: str = (
    f'Время приготовления рецепта не может быть > {RECIPE_CKN_TIME_MAX}.'
)
ING_AMOUNT_MIN_ERR_MSG: str = (
    f'Количество ингредиента в рецепте не может быть < {ING_AMOUNT_MIN}.'
)
ING_AMOUNT_MAX_ERR_MSG: str = (
    f'Количество ингредиента в рецепте не может быть > {ING_AMOUNT_MAX}.'
)
