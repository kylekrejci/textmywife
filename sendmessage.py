import telnyx
import os

telnyx.api_key = os.environ.get('TELNYX_PRIVATE_KEY')

your_telnyx_number = os.environ.get('MY_PHONE_NUMBER')
destination_number = os.environ.get('WIFES_PHONE_NUMBER')

telnyx.Message.create(
    from_=your_telnyx_number,
    to=destination_number,
    text="Leaving now.",
)

