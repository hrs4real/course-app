from enum import Enum
from typing import Optional
from starlette import status
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class LearnType(str, Enum):
    personalised = "personalised"
    group = "group"


class LearnMode(str, Enum):
    assisted = "assisted"
    self = "self"


class UserRole(str, Enum):
    creator = "creator"
    student = "student"


class Course:
    id: int
    name: str
    subject: str
    chapters: int
    no_of_classes: int
    learn_type: LearnType  # personalised, group
    learn_mode: LearnMode  # assisted, self
    user_role: UserRole    # student, creator

    def __init__(self, id, name, subject, chapters, no_of_classes, learn_type, learn_mode, user_role):
        self.id = id
        self.name = name
        self.subject = subject
        self.chapters = chapters
        self.no_of_classes = no_of_classes
        self.learn_type = learn_type
        self.learn_mode = learn_mode
        self.user_role = user_role


class CourseRequest(BaseModel):
    id: Optional[int] = None, Field(title='Id  not needed')
    name: str = Field(min_length=3)
    subject: str = Field(min_length=3)
    chapters: int = Field(gt=0)
    no_of_classes: int = Field(gt=0)
    learn_type: LearnType  # personalised, group
    learn_mode: LearnMode  # assisted, self
    user_role: UserRole

    class Config:
        json_schema_extra={
            'example': {
                    "name": "Your name",
                    "subject": "Science",
                    "chapters": 15,
                    "no_of_classes": 50,
                    "learn_type": "personalised",
                    "learn_mode": "assisted",
                    "user_role": "student"
            }
        }


COURSES = [Course(1, "Harsh", "Science", 15, 50, "personalised", "assisted", "student"),
           Course(2, "Amit", "Maths", 50, 55, "group", "assisted", "creator"),
           Course(3, "Pratham", "Physics", 20, 68, "personalised", "self", "student"),
           Course(4, "Divyansh", "Computer", 15, 72, "group", "self", "student"),
           Course(5, "Shudhanshu", "Chemistry", 25, 70, "group", "assisted", "creator"), ]


@app.get("/course", status_code=status.HTTP_200_OK)
async def get_all_course():
    return COURSES


@app.get("/course/get/{user_role}", status_code=status.HTTP_200_OK )
async def get_filtered_courses(user_role: UserRole):
    course_to_return = []
    for course in COURSES:
        if course.user_role == user_role:
            course_to_return.append(course)
    return course_to_return


@app.post("/course/create/", status_code=status.HTTP_201_CREATED)
async def create_course(course_request: CourseRequest):
    new_course = Course(**course_request.dict())
    COURSES.append(find_course_id(new_course))


def find_course_id(course: Course):
    course.id = 1 if len(COURSES) == 0 else COURSES[-1].id + 1
    return course


@app.put("/course/update", status_code=status.HTTP_204_NO_CONTENT)
async def update_course(updated_course: CourseRequest):
    course_changed = False
    for i in range(len(COURSES)):
        if COURSES[i].id == updated_course.id:
            COURSES[i] = updated_course
            course_changed = True
    if not course_changed:
        raise HTTPException(status_code=404, detail='Item not found')
