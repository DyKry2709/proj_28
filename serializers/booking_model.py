from pydantic import BaseModel, Field

class BookingDates(BaseModel):
    checkin: str
    checkout: str

class BookingResponseModel(BaseModel):
    firstname: str = Field(..., description="Имя гостя, который сделал бронь")
    lastname: str = Field(..., description="Фамилия гостя, который сделал бронь")
    totalprice: int = Field(..., description="Общая стоимость брони")
    depositpaid: bool = Field(..., description="Внесен ли залог или нет")
    bookingdates: dict = Field(..., description="Подобъект, содержащий даты регистрации и выезда")
    additionalneeds: str = Field(None, description="Другие желания гостя")

    class Config:
        allow_population_by_field_name = True


class CreateBookingRequest(BaseModel):
    firstname: str = Field(..., description="Имя гостя, который сделал бронь")
    lastname: str = Field(..., description="Фамилия гостя, который сделал бронь")
    totalprice: int = Field(..., description="Общая стоимость брони")
    depositpaid: bool = Field(..., description="Внесен ли залог или нет")
    bookingdates: BookingDates = Field(..., description="Даты заезда и выезда")
    additionalneeds: str = Field(..., description="Другие желания гостя")

class BookingResponse(BaseModel):
    bookingid: int
    booking: CreateBookingRequest


class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str

class CreateBookingResponse(BaseModel):
    bookingid: int