EMAIL_MAX_LEN = 254
PASSWORD_MAX_LEN = (
    USERNAME_MAX_LEN
) = FIRST_NAME_MAX_LEN = LAST_NAME_MAX_LEN = 150


RECIPE_NAME_MAX_LEN = (
    TAG_NAME_MAX_LEN
) = TAG_SLUG_MAX_LEN = ING_NAME_MAX_LEN = ING_MES_MAX_LEN = 200
TAG_COLOR_MAX_LEN = 7
RECIPE_CKN_TIME_MIN = ING_AMOUNT_MIN = 1
RECIPE_CKN_TIME_MAX = ING_AMOUNT_MAX = 32_000

RECIPE_CKN_TIME_MIN_ERR_MSG = (
    f'Время приготовления рецепта не может быть < {RECIPE_CKN_TIME_MIN}.'
)
RECIPE_CKN_TIME_MAX_ERR_MSG = (
    f'Время приготовления рецепта не может быть > {RECIPE_CKN_TIME_MAX}.'
)
ING_AMOUNT_MIN_ERR_MSG = (
    f'Количество ингредиента в рецепте не может быть < {ING_AMOUNT_MIN}.'
)
ING_AMOUNT_MAX_ERR_MSG = (
    f'Количество ингредиента в рецепте не может быть > {ING_AMOUNT_MAX}.'
)
