def trace():
    try:
        import ipdb; ipdb.set_trace()
    except ImportError:
        import pdb; pdb.set_trace()
    return None