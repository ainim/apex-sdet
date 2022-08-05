HOME_PAGE_LOCATORS = {
    'search_bar': ('ID', 'mainSearchbar'),
    'search_button': ('CLASS_NAME', 'input-group-text'),
    'search_results': ('CSS','ul.row.p-2'),
    'screens_category': ('LINK_TEXT', 'Pantallas'),
    'login': ('CSS', 'span.a-header__topLink')
}

LOGIN_PAGE_LOCATORS = {
    'email': ('ID', 'username'),
    'password': ('ID', 'password'),
    'login_button': ('CSS', 'button[name=action]'),
    'signup': ('LINK_TEXT', 'Crear cuenta')
}

SIGNUP_PAGE_LOCATORS = {
    'email': ('ID', 'email'),
    'password': ('ID', 'password'),
    'signup_button': ('CSS', 'button[name=action]'),
    'login': ('LINK_TEXT', 'Iniciar sesión')
}

PLP_PAGE_LOCATORS = {
    '32in_size_filter': ('ID', 'variants.normalizedSize-32 pulgadas'),
    'lg_brand_filter': ('ID', 'brand-LG'),
    'max_price_filter': ('ID', 'max-price-filter'),
    'min_price_filter': ('ID', 'min-price-filter'),
    'price_filter_button': ('CLASS_NAME', 'a-price__filterButton'),
    'results': ('CLASS_NAME', 'a-plp-results-title'),
    'no_results': ('CLASS_NAME', 'a-headline__results')
}
