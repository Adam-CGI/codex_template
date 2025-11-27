from package_name.main import build_greeting, main


def run_example() -> None:
    print("Running example use...")
    custom = build_greeting("Codex user")
    print(custom)
    main()


if __name__ == "__main__":
    run_example()
