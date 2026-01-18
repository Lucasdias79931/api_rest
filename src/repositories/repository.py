from abc import ABC, abstractmethod


class Repository(ABC):
    
    @abstractmethod
    def save(entity)->None:
        """
            This method must be implemented to persist entity in database        
        """
        pass

    @abstractmethod
    def get_by_id(entity_id):
        """
            This method must be implemented to load entity by id from database      
        """

    @staticmethod
    @property
    @abstractmethod
    def get_all():
         """
            This method must be implemented to load all entities from database      
        """
    @abstractmethod
    def delete_or_mark_inactive(self, entity_id):
        """
            This method must be implemented to delete or mark a entity as inactive in database   
        """
    
    @abstractmethod
    @staticmethod
    def update(entity):
        """
            This method must be implemented to update entity in database  
        """
    
