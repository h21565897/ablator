from pathlib import Path

from ablator.modules.loggers.baselogger import init_logger


def test_base_logger(tmp_path: Path):
    logger = init_logger("test", tmp_path/"test.log")
    logger.info("hello")
    logger.error("world")


if __name__ == "__main__":
    test_base_logger(Path("/tmp"))
