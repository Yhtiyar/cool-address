import rlp
from eth_utils import keccak, to_checksum_address, to_bytes


def mk_contract_address(sender: str, nonce: int) -> str:
    """Create a contract address using eth-utils.

    # https://ethereum.stackexchange.com/a/761/620
    """
    sender_bytes = to_bytes(hexstr=sender)
    raw = rlp.encode([sender_bytes, nonce])
    h = keccak(raw)
    address_bytes = h[12:]
    return to_checksum_address(address_bytes)


def bruteforce_contract_addresses(
    sender: str, nonce_start: int, nonce_end: int
) -> None:
    sender_checksum = to_checksum_address(sender)
    for nonce in range(nonce_start, nonce_end + 1):
        print(
            f"{nonce}->{to_checksum_address(mk_contract_address(sender_checksum, nonce))}"
        )


def main():
    print(
        to_checksum_address(
            mk_contract_address(
                to_checksum_address("0xeba757ceac281d9de85b768ef4b9e1992c41ea7f"), 64
            )
        )
    )

    bruteforce_contract_addresses(
        "0xeba757ceac281d9de85b768ef4b9e1992c41ea7f", 64, 10000
    )


if __name__ == "__main__":
    main()
