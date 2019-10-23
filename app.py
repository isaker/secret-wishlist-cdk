#!/usr/bin/env python3

from aws_cdk import core

from secret_wishlist_cdk.secret_wishlist_cdk_stack import SecretWishlistCdkStack


app = core.App()
SecretWishlistCdkStack(app, "secret-wishlist-cdk")

app.synth()
