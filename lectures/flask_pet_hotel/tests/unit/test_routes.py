import pytest


@pytest.mark.parametrize(
    'url',
    (
        '/check-in',
        '/check-in/'
    )
)
def test_checkin(app, url):
    resp = app.post(url, json='something')
    assert resp.status_code == 200
