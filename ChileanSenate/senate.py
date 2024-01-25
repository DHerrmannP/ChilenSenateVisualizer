from pydantic import BaseModel,PositiveFloat,validator
from datetime import datetime
from typing import Optional, List
from enum import IntEnum,Enum

class Partido(BaseModel):
    id: str
    nombre: str
    alias: str

class Militancia(BaseModel):
    fecha_inicio: datetime
    fecha_termino: datetime
    partido: Partido

class Sexo(IntEnum):
    femenino = 0
    masculino = 1

class Diputado(BaseModel):
    id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    sexo: Sexo
    militancia: Optional[Militancia]

class DetalleDiputado(Diputado):
    nombre2: Optional[str]
    fecha_nacimiento: datetime
    rut: Optional[str]
    rutdv: Optional[str]
    historial_militancias: List[Militancia]


class TipoVotacion(IntEnum):
    proyecto_de_ley = 1
    proyecto_de_resolucion = 2
    proyecto_de_acuerdo = 3
    otros = 4

class TipoVotacionProyectoLey(IntEnum):
    general = 1
    particular = 2
    general_y_particular = 3
    admisibilidad = 4
    cierre_debate = 5
    unica = 6

class ValorVoto(IntEnum):
    no = 0
    si = 1
    abstencion = 2

class Voto(BaseModel):
    diputado: Diputado
    valor: ValorVoto

class TipoResultadoVotacion(IntEnum):
    rechazado = 0
    aprobado = 1
    unanime = 2
    empate = 3
    sin_quorum = 4
    sin_resultadozado = 9

class TipoQuorum(IntEnum):
    simple = 1
    calificado = 2

class Quorum(BaseModel):
    tipo = TipoQuorum
    valor = PositiveFloat

    @validator('valor')
    def invalid_quorum_value(cls, v: PositiveFloat) -> PositiveFloat:
        if v not in [1/2, 1/3, 2/3, 2/5, 3/5]:
            raise ValueError('valor de quorum invalido')
        return v

class Votacion(BaseModel):
    id: int
    descripcion: str
    fecha: datetime
    total_no: int
    total_si: int
    total_abstension: int
    total_dispensado: int
    quorum: Quorum
    tipo: TipoVotacion
    tipo_proyecto_ley: Optional[TipoVotacionProyectoLey]
    votos: List[Voto]
