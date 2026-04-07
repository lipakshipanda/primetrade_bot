from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate a highly secure RSA 2048-bit private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Generate the matching public key
public_key = private_key.public_key()
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save them as files
with open("private_key.pem", "wb") as f:
    f.write(private_bytes)

with open("public_key.pem", "wb") as f:
    f.write(public_bytes)

print("\n✅ Success! Your keys have been generated.")