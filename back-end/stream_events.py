import bot_interaction
import json

from twitivity import Event


class StreamEvent(Event):
    CALLBACK_URL: str = "https://c39615499b6a.ngrok.io/payload"

    def on_data(self, data: json) -> None:
        event_type = list(data.keys())[1]
        if "direct_message_events" == event_type:
            if data["direct_message_events"][0]["message_create"]["sender_id"] != '1328476914600833025':
                bot_interaction.processData(data)


stream_events = StreamEvent()
stream_events.listen()
