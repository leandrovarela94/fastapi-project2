
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.routes.deps import get_db_sesion
from app.schemas.product import Product, ProductInput
from app.use_cases.product import ProductUseCases

router = APIRouter(prefix='/product')


@router.post('/add')
def add_product(
    product_input: ProductInput,
    db_session: Session = Depends(get_db_sesion)
):

    uc = ProductUseCases(db_session=db_session)
    uc.add_product(
        product=product_input.product,
        category_slug=product_input.category_slug
    )

    return Response(status_code=status.HTTP_201_CREATED)
