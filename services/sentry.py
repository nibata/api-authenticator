import sentry_sdk


sentry_sdk.init(
    dsn="https://62700fec85e3e39f7c0fd71497de6e36@o4504623944892416.ingest.us.sentry.io/4507696121643008",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)