import subprocess

from PyInstaller import __main__ as pyi_main


def test_serial_version(tmp_path):
    """Test to validate the PyInstaller app provides the pySerial version."""
    app_name = "granola_test_app"
    workpath = tmp_path / "build"
    distpath = tmp_path / "dist"
    app = (tmp_path / app_name).with_suffix(".py")

    # A simple app to verify that the pySerial version is available in the app
    app.write_text(
        "\n".join(
            [
                u"import pkg_resources",
                u"from granola.utils import check_min_package_version",
                u"pyserial_version = pkg_resources.get_distribution('pyserial').version",
                u"check_min_package_version('pyserial', pyserial_version)",
            ]
        )
    )

    args = [
        # Place all generated failes in the tmp_path.
        "--workpath",
        str(workpath),
        "--distpath",
        str(distpath),
        "--specpath",
        str(tmp_path),
        str(app),
    ]

    # Build the application
    pyi_main.run(args)

    # Run the built application and confirm it does not error
    subprocess.check_call([str(distpath / app_name / app_name)])
