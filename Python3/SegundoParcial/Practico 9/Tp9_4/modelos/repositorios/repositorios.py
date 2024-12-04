from modelos.repositorios.repositorios import RepositorioPoliza

repo_poliza = None

def obtenerRepoPoliza():
    global repo_poliza
    if repo_poliza is None:
        repo_poliza = RepositorioPoliza()
    return repo_poliza