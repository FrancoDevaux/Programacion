from modelos.repositorios.repositorio_alumnos import RepositorioAlumno
from modelos.repositorios.repositorio_temas import RepositorioTema
from modelos.repositorios.repositorio_temaAlumno import RepositorioTemaAlumno

repo_alumnos = None
repo_temas = None
repo_temaAlumnos = None

def obtenerRepoAlumnos()->RepositorioAlumno:
    global repo_alumnos
    if not isinstance(repo_alumnos, RepositorioAlumno):
        repo_alumnos = RepositorioAlumno()
    return repo_alumnos


def obtenerRepoTemas()->RepositorioTema:
    global repo_temas
    if not isinstance(repo_temas, RepositorioTema):
        repo_temas = RepositorioTema()
    return repo_temas

def obtenerRepoTemaAlumnos():
    global repo_temaAlumnos
    if not isinstance(repo_temaAlumnos, RepositorioTemaAlumno):
        repo_temaAlumnos = RepositorioTemaAlumno()
    return repo_temaAlumnos