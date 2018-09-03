# connections 알아보기
from django.db import connections

import decimal
import math

# cursor = connections['Strike10'].cursor()
# cursor.execute("SELECT product_id, ASIN, title, brand, model, feature, weight, cat_prod FROM product WHERE ASIN=%s;", ASIN)
# product = cursor.fetchone()
#
# # product part
# product_id = product[0]
# weight_raw = decimal.Decimal(str(product[6]))
# weight_olim = int(math.ceil(float(product[6])))