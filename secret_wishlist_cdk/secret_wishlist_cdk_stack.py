from aws_cdk import core
from aws_cdk import aws_lambda
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_dynamodb as dynamo

class SecretWishlistCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        create_wishlist_lambda = aws_lambda.Function(
            self,
            id='create-wishlist',
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            code=aws_lambda.Code.asset('lambda'),
            handler='create-wishlist.handler'
        )

        wishlist_api = apigw.LambdaRestApi(
            self,
            id='wishlist-api',
            handler=create_wishlist_lambda
        )

        wishlist_resource = wishlist_api.root.add_resource(path_part='wishlist')
        wishlist_resource.add_method(http_method='POST')

        wishlist_db = dynamo.Table(
            self,
            id='wishlists',
            partition_key=dynamo.Attribute(
                name='id',
                type=dynamo.AttributeType.STRING
            ),
            billing_mode=dynamo.BillingMode.PAY_PER_REQUEST
        )

        create_wishlist_lambda.add_environment(key='wishlistTable', value=wishlist_db.table_name)
        wishlist_db.grant_read_write_data(create_wishlist_lambda)
