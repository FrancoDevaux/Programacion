from modelos.repositorios.repositorio_libro import RepositorioLibro
from modelos.repositorios.repositorio_socio import RepositorioSocio
from modelos.repositorios.repositorio_prestamo import RepositorioPrestamo

repo_libro = None
repo_socio = None
repo_prestamo = None

def obtenerRepoLibro():
    global repo_libro
    if not isinstance(repo_libro, RepositorioLibro):
        repo_libro = RepositorioLibro()
    return repo_libro

def obtenerRepoSocio():
    global repo_socio
    if not isinstance(repo_socio, RepositorioSocio):
        repo_socio = RepositorioSocio()
    return repo_socio

def obtenerRepoPrestamo():
    global repo_prestamo
    if not isinstance(repo_prestamo, RepositorioPrestamo):
        repo_prestamo = RepositorioPrestamo()
    return repo_prestamo