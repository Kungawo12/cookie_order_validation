from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Cookie:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.number_of_boxes= data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookies"
        results= connectToMySQL('cookie_db').query_db(query)
        
        cookies =[]
        for cookie in results:
            cookies.append(cls(cookie))
        return cookies
    
    @classmethod
    def get_one_cookie(cls,data):
        query = """SELECT * FROM cookies
                WHERE id = %(id)s;
                """
        results= connectToMySQL('cookie_db').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def save(cls,data):
        query= """INSERT INTO cookies(name,type,number_of_boxes)
                VALUE (%(name)s, %(type)s, %(number_of_boxes)s)
        """
        return connectToMySQL("cookie_db").query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query= """UPDATE cookies
                SET name = %(name)s, type= %(type)s, number_of_boxes= %(number_of_boxes)s
                WHERE id = %(id)s;
        """
        results = connectToMySQL('cookie_db').query_db(query,data)
        return results
    
    @staticmethod
    def validate_cookie(data):
        is_valid = True
        
        if len(data['name']) <2 and len(data['type'])< 2 and len(data['number_of_boxes']) <=0:
            flash("All fields are required!")
            is_valid=False
        else:
            if len(data['name']) <2:
                flash('Name must be at least 2 characters')
                is_valid= False
            if len(data['type'])< 2:
                flash('Type of cookie must be at least 2 characters')
                is_valid= False
            if len(data['number_of_boxes']) <=0:
                flash('Number of boxes must be positive numbers')
                is_valid = False
        print(flash)
        return is_valid