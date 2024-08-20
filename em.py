def detect_spam(email):
    if email.sender == 'promotions@online.com':
        return SPAM
    if contains (email.title, ['tax', 'review']and domain(email.sender,'online.com')):
        return SPAM
    return GOOD