from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

# Gerar par de chaves
privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

publica = privada.public_key()

documento = b"Documento confidencial da empresa."

# Assinar documento
assinatura = privada.sign(
    documento,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Documento assinado!")

# Verificar assinatura
try:
    publica.verify(
        assinatura,
        documento,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("Assinatura válida!")

except Exception:
    print("Assinatura inválida!")