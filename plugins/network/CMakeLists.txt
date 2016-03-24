find_package(OpenSSL REQUIRED)

set(
  IRODS_NETWORK_PLUGIN_ssl_SOURCES
  ${CMAKE_SOURCE_DIR}/plugins/network/ssl/libssl.cpp
  )

set(
  IRODS_NETWORK_PLUGIN_tcp_SOURCES
  ${CMAKE_SOURCE_DIR}/plugins/network/tcp/libtcp.cpp
  )

set(
  IRODS_NETWORK_PLUGINS
  ssl
  tcp
  )

set(
  IRODS_NETWORK_COMPILE_DEFINTIONS_client
  )

set(
  IRODS_NETWORK_COMPILE_DEFINITIONS_server
  RODS_SERVER
  RODS_CLERVER
  ENABLE_RE
  )

set(
  IRODS_NETWORK_PLUGIN_TYPES
  client
  server
  )

foreach(PLUGIN ${IRODS_NETWORK_PLUGINS})
  foreach(TYPE ${IRODS_NETWORK_PLUGIN_TYPES})
    set(IRODS_CURRENT_PLUGIN_TARGET ${PLUGIN}_${TYPE})

    add_library(
      ${IRODS_CURRENT_PLUGIN_TARGET}
      MODULE
      ${IRODS_NETWORK_PLUGIN_${PLUGIN}_SOURCES}
      )

    target_include_directories(
      ${IRODS_CURRENT_PLUGIN_TARGET}
      PRIVATE
      ${CMAKE_BINARY_DIR}/iRODS/lib/core/include
      ${CMAKE_SOURCE_DIR}/iRODS/lib/core/include
      ${CMAKE_SOURCE_DIR}/iRODS/lib/api/include
      ${CMAKE_SOURCE_DIR}/iRODS/server/drivers/include
      ${CMAKE_SOURCE_DIR}/iRODS/server/core/include
      ${CMAKE_SOURCE_DIR}/iRODS/server/icat/include
      ${CMAKE_SOURCE_DIR}/iRODS/server/re/include
      ${IRODS_EXTERNALS_FULLPATH_BOOST}/include
      ${IRODS_EXTERNALS_FULLPATH_JANSSON}/include
      ${IRODS_EXTERNALS_FULLPATH_ARCHIVE}/include
      ${OPENSSL_INCLUDE_DIR}
      )

    target_link_libraries(
      ${IRODS_CURRENT_PLUGIN_TARGET}
      PRIVATE
      irods_server
      irods_clerver
      ${IRODS_EXTERNALS_FULLPATH_BOOST}/lib/libboost_filesystem.so
      ${IRODS_EXTERNALS_FULLPATH_BOOST}/lib/libboost_system.so
      ${IRODS_EXTERNALS_FULLPATH_ARCHIVE}/lib/libarchive.so
      ${OPENSSL_CRYPTO_LIBRARY}
      ${OPENSSL_SSL_LIBRARY}
      )

    target_compile_definitions(${IRODS_CURRENT_PLUGIN_TARGET} PRIVATE ${IRODS_NETWORK_COMPILE_DEFINTIONS_${TYPE}} ${IRODS_COMPILE_DEFINITIONS} BOOST_SYSTEM_NO_DEPRECATED)
    target_compile_options(${IRODS_CURRENT_PLUGIN_TARGET} PRIVATE -Wno-write-strings)
    set_property(TARGET ${IRODS_CURRENT_PLUGIN_TARGET} PROPERTY CXX_STANDARD ${IRODS_CXX_STANDARD})
    install(
      TARGETS
      ${IRODS_CURRENT_PLUGIN_TARGET}
      LIBRARY
      DESTINATION ${IRODS_HOME_DIRECTORY}/plugins/network
      COMPONENT ${IRODS_PACKAGE_COMPONENT_RUNTIME_NAME}
      )
  endforeach()
endforeach()