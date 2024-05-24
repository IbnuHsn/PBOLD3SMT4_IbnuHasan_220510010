from abc import ABC, abstractmethod

class Doseninterface(ABC):
    @abstractmethod
    def all():
        pass

    @abstractmethod
    def store(matakuliah_obj):
        pass

    @abstractmethod
    def find(matakuliah_id):
        pass

    @abstractmethod
    def update(matakulliah_id, matakuliah_obj):
        pass

    @abstractmethod
    def delete(matakulliah_id):
        pass