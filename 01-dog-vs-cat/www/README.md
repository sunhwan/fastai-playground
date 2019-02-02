# deploy to heroku

See https://devcenter.heroku.com/articles/container-registry-and-runtime for more detailed explanation.

    heroku container:login
    heroku create
    heroku container:push web
    heroku container:release web
    heroku open
