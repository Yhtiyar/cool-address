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
                to_checksum_address("0xf857be06f23d2efb5bdc2916d07b302a875b6d2f"), 0
            )
        )
    )

    bruteforce_contract_addresses(
        "0xf857be06f23d2efb5bdc2916d07b302a875b6d2f", 0, 10000
    )


if __name__ == "__main__":
    main()
