"""module."""

from notty.dev.artifacts.builder.builder import NottyBuilder


class TestNottyBuilder:
    """Test class."""

    def test_get_additional_resource_pkgs(self) -> None:
        """Test method."""
        datas = NottyBuilder.get_additional_resource_pkgs()
        assert isinstance(datas, list), f"Expected list, got {type(datas)}"
