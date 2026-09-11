
# Transaction Token

Stored transaction token resource. `payment_type` discriminates which variant applies — and therefore the concrete shape of `data` — per the mapping above.

## Data Type

`CardTransactionToken | KonbiniTransactionToken | OnlineTransactionToken | BankTransferTransactionToken | PaidyTransactionToken | QrScanTransactionToken | QrMerchantTransactionToken`

## Cases

| Type |
|  --- |
| [`CardTransactionToken`](../../../doc/models/card-transaction-token.md) |
| [`KonbiniTransactionToken`](../../../doc/models/konbini-transaction-token.md) |
| [`OnlineTransactionToken`](../../../doc/models/online-transaction-token.md) |
| [`BankTransferTransactionToken`](../../../doc/models/bank-transfer-transaction-token.md) |
| [`PaidyTransactionToken`](../../../doc/models/paidy-transaction-token.md) |
| [`QrScanTransactionToken`](../../../doc/models/qr-scan-transaction-token.md) |
| [`QrMerchantTransactionToken`](../../../doc/models/qr-merchant-transaction-token.md) |

## CardTransactionToken

### Initialization Code

#### Example

```python
value = CardTransactionToken(
    data=TokenResponseCardData(
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
    ),
    id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
    store_id='fc264608-9a9e-495e-844e-a08129a81af4',
    email='test@univapay.com',
    active=True,
    mode=TransactionTokenMode.LIVE,
    mtype=TransactionTokenType.ONE_TIME,
    usage_limit='example',
    confirmed=True,
    metadata={
        'customer_id': 'cust_12345'
    },
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    last_used_on=dateutil.parser.parse('2026-04-09T07:35:50Z')
)
```

## KonbiniTransactionToken

### Initialization Code

#### Example

```python
value = KonbiniTransactionToken(
    data=TokenResponseKonbiniData(
        customer_name='Taro Yamada',
        convenience_store=BaseKonbiniDataConvenienceStore.SEVEN_ELEVEN,
        expiration_period='P7D',
        expiration_time_shift=None,
        phone_number=TokenResponsePhoneNumber(
            country_code=81,
            local_number='08012341234'
        )
    ),
    id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
    store_id='fc264608-9a9e-495e-844e-a08129a81af4',
    email='test@univapay.com',
    active=True,
    mode=TransactionTokenMode.LIVE,
    mtype=TransactionTokenType.ONE_TIME,
    usage_limit='example',
    confirmed=True,
    metadata={
        'customer_id': 'cust_12345'
    },
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    last_used_on=dateutil.parser.parse('2026-04-09T07:35:50Z')
)
```

## OnlineTransactionToken

### Initialization Code

#### Example

```python
value = OnlineTransactionToken(
    data=TokenResponseOnlineData(
        brand=BaseOnlineDataBrand.WE_CHAT_ONLINE,
        call_method=BaseOnlineDataCallMethod.WEB,
        user_identifier='wechat_open_id_12345'
    ),
    id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
    store_id='fc264608-9a9e-495e-844e-a08129a81af4',
    email='test@univapay.com',
    active=True,
    mode=TransactionTokenMode.LIVE,
    mtype=TransactionTokenType.ONE_TIME,
    usage_limit='example',
    confirmed=True,
    metadata={
        'customer_id': 'cust_12345'
    },
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    last_used_on=dateutil.parser.parse('2026-04-09T07:35:50Z')
)
```

## BankTransferTransactionToken

### Initialization Code

#### Example

```python
value = BankTransferTransactionToken(
    data=TokenResponseBankTransferData(
        brand='aozora_bank',
        expiration_period='PT168H',
        expiration_time_shift='23:59:59+09:00',
        bank_code='0310',
        bank_name='GMOあおぞらネット銀行',
        branch_code='123',
        branch_name='Test Branch',
        account_number='1234567',
        account_holder_name='TARO YAMADA'
    ),
    id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
    store_id='fc264608-9a9e-495e-844e-a08129a81af4',
    email='test@univapay.com',
    active=True,
    mode=TransactionTokenMode.LIVE,
    mtype=TransactionTokenType.ONE_TIME,
    usage_limit='example',
    confirmed=True,
    metadata={
        'customer_id': 'cust_12345'
    },
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    last_used_on=dateutil.parser.parse('2026-04-09T07:35:50Z')
)
```

## PaidyTransactionToken

### Initialization Code

#### Example

```python
value = PaidyTransactionToken(
    data=TokenResponsePaidyData(
        paidy_token='paidy-token-abc123',
        phone_number='08012341234',
        shipping_address=TokenResponsePaidyDataShippingAddress(
            zip='105-0011',
            line_1='1-1-1',
            city='Minato',
            state='Tokyo'
        )
    ),
    id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
    store_id='fc264608-9a9e-495e-844e-a08129a81af4',
    email='test@univapay.com',
    active=True,
    mode=TransactionTokenMode.LIVE,
    mtype=TransactionTokenType.ONE_TIME,
    usage_limit='example',
    confirmed=True,
    metadata={
        'customer_id': 'cust_12345'
    },
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    last_used_on=dateutil.parser.parse('2026-04-09T07:35:50Z')
)
```

## QrScanTransactionToken

### Initialization Code

#### Example

```python
value = QrScanTransactionToken(
    data=TokenResponseQrScanData(
        brand='pay_pay'
    ),
    id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
    store_id='fc264608-9a9e-495e-844e-a08129a81af4',
    email='test@univapay.com',
    active=True,
    mode=TransactionTokenMode.LIVE,
    mtype=TransactionTokenType.ONE_TIME,
    usage_limit='example',
    confirmed=True,
    metadata={
        'customer_id': 'cust_12345'
    },
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    last_used_on=dateutil.parser.parse('2026-04-09T07:35:50Z')
)
```

## QrMerchantTransactionToken

### Initialization Code

#### Example

```python
value = QrMerchantTransactionToken(
    data=TokenResponseQrMerchantData(
        qr_image_url='71001234567890202604141200450',
        brand='pay_pay_merchant'
    ),
    id='6426bbd2-17bd-41bf-883b-1fe970db48ee',
    store_id='fc264608-9a9e-495e-844e-a08129a81af4',
    email='test@univapay.com',
    active=True,
    mode=TransactionTokenMode.LIVE,
    mtype=TransactionTokenType.ONE_TIME,
    usage_limit='example',
    confirmed=True,
    metadata={
        'customer_id': 'cust_12345'
    },
    created_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    updated_on=dateutil.parser.parse('2026-04-09T07:35:50Z'),
    last_used_on=dateutil.parser.parse('2026-04-09T07:35:50Z')
)
```

