import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Starter"
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT_JSON: bool = True

    def __init__(self, **kwargs):
        env = os.getenv("ENV", "dev")
        env_candidates = [".env", f".env.{env}"]
        env_files = [path for path in env_candidates if os.path.exists(path)]
        if "model_config" not in kwargs:
            if env_files:
                kwargs["model_config"] = SettingsConfigDict(
                    env_file=env_files, env_file_encoding="utf-8"
                )
        super().__init__(**kwargs)


# 单例模式的 settings 实例
_settings: Settings | None = None


def get_settings() -> Settings:
    """获取 settings 实例（单例模式，延迟初始化）"""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings


def reload_settings() -> Settings:
    """重新加载 settings 实例（用于环境切换）"""
    global _settings
    _settings = Settings()
    return _settings


# 导出 settings 实例以保持向后兼容
settings = get_settings()
