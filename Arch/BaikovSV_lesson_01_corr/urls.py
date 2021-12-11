import views

fronts = [views.opposite_color_front, views.similar_color_front]

routes = {
    '/': views.index_view,
    '/black/': views.black_view,
    '/red/': views.red_view,
    '/white/': views.white_view,
    '/other/': views.Other()
}
