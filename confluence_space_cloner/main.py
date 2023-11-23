from dotenv import load_dotenv

from lib import confluence
from lib.config import Config, get_config


def main(config: Config):
    # Get source space
    source_space = confluence.get_space(
        confluence_domain=config.confluence_domain,
        username=config.username,
        api_token=config.api_token,
        space_id="abc123",
    )

    print(f"Source space: {source_space}")

    # Create destination space
    confluence.create_space(
        api_token=config.api_token,
        confluence_domain=config.confluence_domain,
        space_id="xyz123",
        space_name="Cloned space name",
    )


if __name__ == "__main__":
    load_dotenv()
    config = get_config()
    main(config=config)
