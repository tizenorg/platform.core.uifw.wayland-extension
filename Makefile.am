INCLUDES = -I$(top_builddir)/protocol -I$(top_srcdir)/src

pkgconfigdir = $(libdir)/pkgconfig
protocoldir = $(libdir)/wayland-extension
protocolincludedir = $(includedir)/wayland-extension

pkgconfig_DATA =
protocolinclude_HEADERS = src/wayland-extension-version.h
protocol_LTLIBRARIES =

### protocol.[ch]
protocol/%-protocol.c : $(top_srcdir)/protocol/%.xml
	$(wayland_scanner) code < $< > $@
protocol/%-server-protocol.h : $(top_srcdir)/protocol/%.xml
	$(wayland_scanner) server-header < $< > $@
protocol/%-client-protocol.h : $(top_srcdir)/protocol/%.xml
	$(wayland_scanner) client-header < $< > $@

### protocol.pc
src/%-server.pc : $(top_srcdir)/src/template-server.pc
	$(cp) $< $@ && $(perl) -pi -e 's|template|$*|g' $@
src/%-client.pc : $(top_srcdir)/src/template-client.pc
	$(cp) $< $@ && $(perl) -pi -e 's|template|$*|g' $@

### xdg-shell
protocol_LTLIBRARIES += \
	libxdg-shell-server.la \
	libxdg-shell-client.la
pkgconfig_DATA += \
	src/xdg-shell-server.pc \
	src/xdg-shell-client.pc
protocolinclude_HEADERS += \
	protocol/xdg-shell-server-protocol.h \
	protocol/xdg-shell-client-protocol.h
libxdg_shell_server_la_SOURCES = protocol/xdg-shell-protocol.c
libxdg_shell_client_la_SOURCES = protocol/xdg-shell-protocol.c

### input-method
protocol_LTLIBRARIES += \
	libinput-method-server.la \
	libinput-method-client.la
pkgconfig_DATA += \
	src/input-method-server.pc \
	src/input-method-client.pc
protocolinclude_HEADERS += \
	protocol/input-method-server-protocol.h \
	protocol/input-method-client-protocol.h
libinput_method_server_la_SOURCES = protocol/input-method-protocol.c
libinput_method_client_la_SOURCES = protocol/input-method-protocol.c

### fullscreen-shell
protocol_LTLIBRARIES += \
	libfullscreen-shell-server.la \
	libfullscreen-shell-client.la
pkgconfig_DATA += \
	src/fullscreen-shell-server.pc \
	src/fullscreen-shell-client.pc
protocolinclude_HEADERS += \
	protocol/fullscreen-shell-server-protocol.h \
	protocol/fullscreen-shell-client-protocol.h
libfullscreen_shell_server_la_SOURCES = protocol/fullscreen-shell-protocol.c
libfullscreen_shell_client_la_SOURCES = protocol/fullscreen-shell-protocol.c

### scaler
protocol_LTLIBRARIES += \
	libscaler-server.la \
	libscaler-client.la
pkgconfig_DATA += \
	src/scaler-server.pc \
	src/scaler-client.pc
protocolinclude_HEADERS += \
	protocol/scaler-server-protocol.h \
	protocol/scaler-client-protocol.h
libscaler_server_la_SOURCES = protocol/scaler-protocol.c
libscaler_client_la_SOURCES = protocol/scaler-protocol.c

### screenshooter
protocol_LTLIBRARIES += \
	libscreenshooter-server.la \
	libscreenshooter-client.la
pkgconfig_DATA += \
	src/screenshooter-server.pc \
	src/screenshooter-client.pc
protocolinclude_HEADERS += \
	protocol/screenshooter-server-protocol.h \
	protocol/screenshooter-client-protocol.h
libscreenshooter_server_la_SOURCES = protocol/screenshooter-protocol.c
libscreenshooter_client_la_SOURCES = protocol/screenshooter-protocol.c

### text-cursor-position
protocol_LTLIBRARIES += \
	libtext-cursor-position-server.la \
	libtext-cursor-position-client.la
pkgconfig_DATA += \
	src/text-cursor-position-server.pc \
	src/text-cursor-position-client.pc
protocolinclude_HEADERS += \
	protocol/text-cursor-position-server-protocol.h \
	protocol/text-cursor-position-client-protocol.h
libtext_cursor_position_server_la_SOURCES = protocol/text-cursor-position-protocol.c
libtext_cursor_position_client_la_SOURCES = protocol/text-cursor-position-protocol.c

### text
protocol_LTLIBRARIES += \
	libtext-server.la \
	libtext-client.la
pkgconfig_DATA += \
	src/text-server.pc \
	src/text-client.pc
protocolinclude_HEADERS += \
	protocol/text-server-protocol.h \
	protocol/text-client-protocol.h
libtext_server_la_SOURCES = protocol/text-protocol.c
libtext_client_la_SOURCES = protocol/text-protocol.c

### tizen-buffer-pool
protocol_LTLIBRARIES += \
	libtizen-buffer-pool-server.la \
	libtizen-buffer-pool-client.la
pkgconfig_DATA += \
	src/tizen-buffer-pool-server.pc \
	src/tizen-buffer-pool-client.pc
protocolinclude_HEADERS += \
	protocol/tizen-buffer-pool-server-protocol.h \
	protocol/tizen-buffer-pool-client-protocol.h
libtizen_buffer_pool_server_la_SOURCES = protocol/tizen-buffer-pool-protocol.c
libtizen_buffer_pool_client_la_SOURCES = protocol/tizen-buffer-pool-protocol.c

### tizen-extension
protocol_LTLIBRARIES += \
	libtizen-extension-server.la \
	libtizen-extension-client.la
pkgconfig_DATA += \
	src/tizen-extension-server.pc \
	src/tizen-extension-client.pc
protocolinclude_HEADERS += \
	protocol/tizen-extension-server-protocol.h \
	protocol/tizen-extension-client-protocol.h
libtizen_extension_server_la_SOURCES = protocol/tizen-extension-protocol.c
libtizen_extension_client_la_SOURCES = protocol/tizen-extension-protocol.c

### keyrouter
protocol_LTLIBRARIES += \
	libkeyrouter-server.la \
	libkeyrouter-client.la
pkgconfig_DATA += \
	src/keyrouter-server.pc \
	src/keyrouter-client.pc
protocolinclude_HEADERS += \
	protocol/keyrouter-server-protocol.h \
	protocol/keyrouter-client-protocol.h
libkeyrouter_server_la_SOURCES = protocol/keyrouter-protocol.c
libkeyrouter_client_la_SOURCES = protocol/keyrouter-protocol.c

### tizen-policy
protocol_LTLIBRARIES += \
	libtizen-policy-server.la \
	libtizen-policy-client.la
pkgconfig_DATA += \
	src/tizen-policy-server.pc \
	src/tizen-policy-client.pc
protocolinclude_HEADERS += \
	protocol/tizen-policy-server-protocol.h \
	protocol/tizen-policy-client-protocol.h
libtizen_policy_server_la_SOURCES = protocol/tizen-policy-protocol.c
libtizen_policy_client_la_SOURCES = protocol/tizen-policy-protocol.c

### quickpanel
protocol_LTLIBRARIES += \
	libquickpanel-server.la \
	libquickpanel-client.la
pkgconfig_DATA += \
	src/quickpanel-server.pc \
	src/quickpanel-client.pc
protocolinclude_HEADERS += \
	protocol/quickpanel-server-protocol.h \
	protocol/quickpanel-client-protocol.h
libquickpanel_server_la_SOURCES = protocol/quickpanel-protocol.c
libquickpanel_client_la_SOURCES = protocol/quickpanel-protocol.c

### tizen-screenshooter
protocol_LTLIBRARIES += \
	libtizen-screenshooter-server.la \
	libtizen-screenshooter-client.la
pkgconfig_DATA += \
	src/tizen-screenshooter-server.pc \
	src/tizen-screenshooter-client.pc
protocolinclude_HEADERS += \
	protocol/tizen-screenshooter-server-protocol.h \
	protocol/tizen-screenshooter-client-protocol.h
libtizen_screenshooter_server_la_SOURCES = protocol/tizen-screenshooter-protocol.c
libtizen_screenshooter_client_la_SOURCES = protocol/tizen-screenshooter-protocol.c

### tizen-subsurface
protocol_LTLIBRARIES += \
	libtizen-subsurface-server.la \
	libtizen-subsurface-client.la
pkgconfig_DATA += \
	src/tizen-subsurface-server.pc \
	src/tizen-subsurface-client.pc
protocolinclude_HEADERS += \
	protocol/tizen-subsurface-server-protocol.h \
	protocol/tizen-subsurface-client-protocol.h
libtizen_subsurface_server_la_SOURCES = protocol/tizen-subsurface-protocol.c
libtizen_subsurface_client_la_SOURCES = protocol/tizen-subsurface-protocol.c

### tizen-transient-for
protocol_LTLIBRARIES += \
	libtizen-transient-for-server.la \
	libtizen-transient-for-client.la
pkgconfig_DATA += \
	src/tizen-transient-for-server.pc \
	src/tizen-transient-for-client.pc
protocolinclude_HEADERS += \
	protocol/tizen-transient-for-server-protocol.h \
	protocol/tizen-transient-for-client-protocol.h
libtizen_transient_for_server_la_SOURCES = protocol/tizen-transient-for-protocol.c
libtizen_transient_for_client_la_SOURCES = protocol/tizen-transient-for-protocol.c
