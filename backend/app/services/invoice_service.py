from sqlalchemy.orm import Session

from app.models.invoice import Invoice
from app.models.sequence import NumberSequence
from app.schemas import InvoiceCreate


class InvoiceService:

    @staticmethod
    def generate_invoice_number(db: Session):

        sequence = db.query(NumberSequence).first()

        if sequence is None:

            sequence = NumberSequence(
                prefix="2026",
                next_number=1,
                digits=4
            )

            db.add(sequence)
            db.commit()
            db.refresh(sequence)

        invoice_number = (
            sequence.prefix +
            str(sequence.next_number).zfill(sequence.digits)
        )

        sequence.next_number += 1

        db.commit()

        return invoice_number

    @staticmethod
    def calculate_totals(amount: float, use_vat: bool):

        if use_vat:

            subtotal = round(amount / 1.21, 2)

            vat = round(amount - subtotal, 2)

            total = amount

        else:

            subtotal = amount

            vat = 0

            total = amount

        return subtotal, vat, total

    @staticmethod
    def create_invoice(db: Session, data: InvoiceCreate):

        subtotal, vat_amount, total = InvoiceService.calculate_totals(
            data.amount,
            data.use_vat
        )

        invoice = Invoice(

            invoice_number=InvoiceService.generate_invoice_number(db),

            customer_id=data.customer_id,

            vehicle_id=data.vehicle_id,

            issue_date=data.issue_date,

            due_date=data.due_date,

            subtotal=subtotal,

            vat_rate=21 if data.use_vat else 0,

            vat_amount=vat_amount,

            total=total,

            use_vat=data.use_vat,

            note=data.note,

            paid=False

        )

        db.add(invoice)

        db.commit()

        db.refresh(invoice)

        return invoice
