import sys
import os
print(sys.path)
print(os.getenv("REDSHIFT_ENDPOINT"))
print(os.getenv("REDSHIFT_USER"))
print(os.getenv("REDSHIFT_PASS"))