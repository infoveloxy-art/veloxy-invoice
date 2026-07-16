from sqlalchemy.orm import Session

from app.models.sequence import NumberSequence


class SequenceService:

    @staticmethod
    def get_next_invoice_number(db: Session):

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

        number = (
            sequence.prefix
            + str(sequence.next_number).zfill(sequence.digits)
        )

        sequence.next_number += 1

        db.commit()

        return number
