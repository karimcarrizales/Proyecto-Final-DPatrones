"""
Pruebas del patrón Singleton.
"""

from src.config.configuracion import ConfiguracionApp


def test_singleton_instancia_unica():

    config1 = ConfiguracionApp()
    config2 = ConfiguracionApp()

    assert config1 is config2