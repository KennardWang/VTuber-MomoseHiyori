import importlib
import pkg_resources
import packaging.version as pv


def test_module_install_cpu():
    modules = ['dlib']

    # Test dlib module
    try:
        # Test import
        m0 = importlib.import_module(modules[0])
        assert m0 is not None

    except ModuleNotFoundError:
        assert False, f"Module {modules[0]} is not correctly installed."


def test_module_install_gpu():
    modules = ['scipy', 'torch']

    # Test scipy module
    try:
        # Test import
        m0 = importlib.import_module(modules[0])
        assert m0 is not None

        # Test version
        v0 = pkg_resources.get_distribution(modules[0]).version
        assert v0 is not None

        # Convert the version to a float and compare
        assert pv.parse(v0) > pv.parse('0.16')

    except ModuleNotFoundError:
        assert False, f"Module {modules[0]} is not correctly installed."

    # Test torch module
    try:
        # Test import
        m1 = importlib.import_module(modules[1])
        assert m1 is not None

        # Test version
        v1 = pkg_resources.get_distribution(modules[1]).version
        assert v1 is not None
        print(v1)

        # Test CUDA
        print(m1.__version__)
        # assert m1.cuda.is_available()

    except ModuleNotFoundError:
        assert False, f"Module {modules[1]} is not correctly installed."
