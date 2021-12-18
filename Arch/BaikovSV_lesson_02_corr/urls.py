import views

fronts = [views.secret_front, views.other_front]

routes = {
    '/': views.Index(),
    '/index/': views.Index(),
    '/about/': views.About(),
    '/contact/': views.Contact(),
}
