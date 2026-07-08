
# Transaction Token Data

Transaction token data payload. The actual structure depends on `payment_type` — card, konbini, online (QR / 3DS), or bank transfer.

## Data Type

`TokenResponseCardData | TokenResponseKonbiniData | TokenResponseOnlineData | TokenResponseBankTransferData`

## Cases

| Type |
|  --- |
| [`TokenResponseCardData`](../../../doc/models/token-response-card-data.md) |
| [`TokenResponseKonbiniData`](../../../doc/models/token-response-konbini-data.md) |
| [`TokenResponseOnlineData`](../../../doc/models/token-response-online-data.md) |
| [`TokenResponseBankTransferData`](../../../doc/models/token-response-bank-transfer-data.md) |

## TokenResponseCardData

### Initialization Code

#### Example

```python
value = TokenResponseCardData(
    card=TokenResponseCardDataCard(
        cardholder='TARO YAMADA',
        exp_month=12,
        exp_year=2026,
        card_bin='424242',
        last_four='4242',
        brand='visa',
        card_type='credit',
        country='JP',
        category='standard',
        issuer=None,
        sub_brand='none'
    ),
    billing=TokenResponseCardDataBilling(
        line_1='1-1-1',
        line_2='Shibakoen',
        state='Tokyo',
        city='Minato',
        country='JP',
        zip='105-0011',
        phone_number=TokenResponsePhoneNumber(
            country_code=81,
            local_number='08012341234'
        )
    ),
    cvv_authorize=TokenResponseCardDataCvvAuthorize(
        enabled=True,
        status='successful',
        charge_id=None,
        credentials_id=None,
        currency='JPY'
    ),
    cvv_authorize_check=TokenResponseCardDataCvvAuthorizeCheck(
        status='successful',
        charge_id=None,
        date=dateutil.parser.parse('2026-04-09T07:35:50Z')
    ),
    three_ds=TokenResponseCardDataThreeDs(
        enabled=True,
        status=TokenResponseCardDataThreeDsStatus.SUCCESSFUL,
        redirect_endpoint=None,
        redirect_id=None,
        exempted=False,
        error=None
    )
)
```

## TokenResponseKonbiniData

### Initialization Code

#### Example

```python
value = TokenResponseKonbiniData(
    customer_name='Taro Yamada',
    convenience_store=BaseKonbiniDataConvenienceStore.SEVEN_ELEVEN,
    expiration_period='P7D',
    expiration_time_shift=None,
    phone_number=TokenResponsePhoneNumber(
        country_code=81,
        local_number='08012341234'
    )
)
```

## TokenResponseOnlineData

### Initialization Code

#### Example

```python
value = TokenResponseOnlineData(
    brand=BaseOnlineDataBrand.WE_CHAT_ONLINE,
    call_method=BaseOnlineDataCallMethod.WEB,
    user_identifier='wechat_open_id_12345'
)
```

## TokenResponseBankTransferData

### Initialization Code

#### Example

```python
value = TokenResponseBankTransferData(
    brand='aozora_bank',
    expiration_period='PT168H',
    expiration_time_shift='23:59:59+09:00',
    bank_code='0310',
    bank_name='GMOあおぞらネット銀行',
    branch_code='123',
    branch_name='Test Branch',
    account_number='1234567',
    account_holder_name='TARO YAMADA'
)
```

