from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# USER DATA
users_data = {
    1:{
        "id":1,
        "name": "Rama Swamy",
        "age": 30
    },
    2:{
        "id":2,
        "name": "Sourab",
        "age": 22
    }
}



@router.get('/')
def get_all_users():
    return {"data": users_data} 


@router.get('/{user_id}')
def get_user(user_id: int):
    if user_id in users_data:
        return users_data[user_id]
    else:
        return {"message": "user data not found"}