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
