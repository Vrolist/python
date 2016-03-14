

from sqlalchemy import or_, and_, not_, desc


gifts = WheelGifts.query.filter(WheelGifts.activity_id==activity_id).all()